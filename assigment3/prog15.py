def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File contents:")
        print(content)

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        if 'file' in locals() and not file.closed:
            file.close()  
read_file('file.txt')