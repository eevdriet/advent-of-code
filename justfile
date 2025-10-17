curr_day := `date +%d`
curr_year := `date +%Y`

get year=curr_year day=curr_day:
    #!/usr/bin/bash
    echo "GET"

    if [[ -z "{{year}}" || -z "{{day}}" ]]; then
        exit 0
    fi

    padded_day=$(printf "%02d" $((10#{{day}})))
    INPUT_FILE="{{justfile_directory()}}/data/{{year}}/$padded_day.input"

    if [[ -f "$INPUT_FILE" ]]; then
        echo "Already have info file"
        exit 0
    fi

    INFO_FILE="{{justfile_directory()}}/data/{{year}}/$padded_day.json"

    source python/.venv/bin/activate
    python "{{justfile_directory()}}/scripts/get_input.py" --day {{day}} --year {{year}} --out $INFO_FILE

create year=curr_year day=curr_day +languages='python': (get year day)
    #!/usr/bin/bash

    if [[ -z "{{year}}" || -z "{{day}}" ]]; then
        exit 0
    fi

    source python/.venv/bin/activate

    # Get input, examples and problem statement
    just get {{year}} {{day}}

    # Extract additional information
    padded_day=$(printf "%02d" $((10#{{day}})))
    INFO_FILE="{{justfile_directory()}}/data/{{year}}/$padded_day.json"

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

    rm -rf INFO_FILE


test year='' day='': (create year day)
    #!/usr/bin/bash
    # Go to the invokation directory and determine language from there
    dir="{{invocation_directory()}}"
    cd $dir || exit 1

    declare -A test_dirs
    test_dirs[rust]="."
    test_dirs[python]="test"

    lang=$(basename $dir)

    find_test_directory() {
        # Verify whether a test directory exists for the given language
        if [[ ! -v test_dirs[$lang] ]]; then
            echo "❌ Unsupported language: $lang"
            return 1
        fi

        # Retrieve the base path for the language including the year
        local dir=${test_dirs[$lang]}
        [[ -n "{{year}}" ]] && dir="$dir/_{{year}}"

        if [[ -n "{{day}}" ]]; then
            padded_day=$(printf "%02d" $((10#{{day}})))

            case $lang in
                python)
                    dir="$dir/test_$padded_day*"
                    ;;

                rust)
                    dir=$(ls $dir | grep -E "^day-$padded_day")
                    ;;
            esac
        fi

        echo $dir
    }

    test_directory=$(find_test_directory)

    case $lang in
        rust)
            cargo watch -s "cargo nextest run -p $test_directory"
            ;;
        python)
            source "{{justfile_directory()}}/python/.venv/bin/activate"
            uv run ptw . --now -- $test_directory
            ;;
        *)
            echo "❌ Unsupported language: $lang"
            return 1
            ;;
    esac
