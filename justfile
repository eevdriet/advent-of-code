curr_day := `date +%d`
curr_year := `date +%Y`

get day=curr_day year=curr_year:
    #!/usr/bin/env bash

    INFO_FILE="{{justfile_directory()}}/data/{{year}}/{{day}}.json"
    python "{{justfile_directory()}}/scripts/get_input.py" --day {{day}} --year {{year}} > $INFO_FILE

create day=curr_day year=curr_year +languages='rust':
    #!/usr/bin/env bash

    source "{{justfile_directory()}}/python/.venv/bin/activate"

    # Get input, examples and problem statement
    just get {{day}} {{year}}

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

work-rust day=curr_day part='1':
    #!/usr/bin/env bash

    # Extract information for the problem
    padded_day=$(printf "%02d" {{day}})

    cargo watch -w "${padded_day}*" -s "just test-rust {{day}} {{part}}"

test-rust day=curr_day part='1':
    #!/usr/bin/env bash

    # Extract information for the problem
    padded_day=$(printf "%02d" {{day}})

    cargo nextest run -p "${padded_day}*" part{{part}}
    
