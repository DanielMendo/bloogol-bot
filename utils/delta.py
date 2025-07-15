import json

def convert_to_delta(lines, images=[]):
    delta = []
    img_index = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue

        is_subtitle = len(stripped.split()) <= 8 and not stripped.endswith(".")

        if is_subtitle:
            delta.append({"insert": stripped + "\n", "attributes": {"header": 3}})
        else:
            delta.append({"insert": stripped + "\n"})

        delta.append({"insert": "\n"})
        
        if not is_subtitle and img_index < len(images):
            delta.append({
                "insert": {
                    "image": images[img_index]
                },
                "attributes": {
                    "style": "width: 100%; height: auto;"
                }
            })
            delta.append({"insert": "\n"})
            delta.append({"insert": "\n"})
            img_index += 1

    return json.dumps(delta, ensure_ascii=False)

