import sys
import shutil
from pathlib import Path

def process_files(src_dir, dst_dir):
    src_path = Path(src_dir)
    dst_path = Path(dst_dir)

    try:
        if not dst_path.exists():
            dst_path.mkdir(parents=True)

        for item in src_path.iterdir():
            if item.is_dir():
                process_files(item, dst_path)
            elif item.is_file():
                file_extension = item.suffix[1:] if item.suffix else 'no_ext'

                ext_dir = dst_path / file_extension
                if not ext_dir.exists():
                    ext_dir.mkdir(parents=True)

                shutil.copy2(item, ext_dir / item.name)
                print(f"Copy {item} to {ext_dir / item.name}")

    except Exception as e:
        print(f"Error: {e}")

def main(arguments):
    src = arguments[1]
    dest = "dist"
    try:
        dest = arguments[2]
    except IndexError:
        pass

    print(src, dest)
    process_files(src, dest)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
       print(f"Please provide arguments: {sys.argv[0]} <src-path> <dest-path>")
    else:
       main(sys.argv)
       
    # main([None, "."])
       