curr_day := `date +%d`
curr_year := `date +%Y`

get year=curr_year day=curr_day:
    #!/usr/bin/bash
    source "{{justfile_directory()}}/python/.venv/bin/activate"

    INFO_FILE="{{justfile_directory()}}/data/{{year}}/{{day}}.json"
    python "{{justfile_directory()}}/scripts/get_input.py" --day {{day}} --year {{year}} > $INFO_FILE

create year=curr_year day=curr_day +languages='python':
    #!/usr/bin/bash
    source "{{justfile_directory()}}/python/.venv/bin/activate"

    # Get input, examples and problem statement
    just get {{year}} {{day}}

    # Extract additional information
    INFO_FILE="{{justfile_directory()}}/data/{{year}}/{{day}}.json"

    padded_day=$(jq -r .padded_day $INFO_FILE)
    title=$(jq -r .title $INFO_FILE)
    text=$(jq -r .text $INFO_FILE)
    slug=$(jq -r .slug $INFO_FILE)

    # Create an Obsidian note
    python "{{justfile_directory()}}/scripts/create_note.py" {{day}} {{year}} "{{languages}}"

    # Create the templates(s) for each of the chosen languages
    for lang in {{languages}}; do
        case "$lang" in
            # Use cargo generate
            rust)
                cargo generate \
                    --path "{{justfile_directory()}}/templates/rust" \
                    --destination "{{justfile_directory()}}/rust/_{{year}}" \
                    --name "day-$padded_day-$slug" \
                    --define day={{day}} \
                    --define slug="$slug" \
                    --define title="$title" \
                    --define year={{year}} \
                    --silent
                ;;
            python)
                python scripts/create_template.py {{day}} {{year}} "$lang"
                ;;
            *)
                echo "❌ Unsupported language: $lang"
                ;;
        esac
    done

    # Remove information file
    rm -f $INFO_FILE


test year=curr_year day=curr_day part='1':
    #!/usr/bin/bash
    dir="{{invocation_directory()}}"
    cd $dir || exit 1

    padded_day=$(printf "%02d" $((10#{{day}})))
    lang=$(basename $dir)

    case $lang in
        rust)
            day_folder=$(ls $dir/_{{year}}/ | grep -E "^day-$padded_day")
            echo "DAY_FO: $day_folder"
            cargo watch -s "cargo nextest run -p $day_folder"
            ;;
        python)
            source "{{justfile_directory()}}/python/.venv/bin/activate"
            uv run ptw . --now -- $lang/test/_{{year}}/test_$padded_day*
            ;;
        *)
            echo "❌ Unsupported language: $lang"
            ;;
    esac
