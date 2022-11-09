import pickle

def save_file(list_to_save, filename="alumnos.stu"):
    with open(f"data/{filename}", "wb") as f:
        pickle.dump(list_to_save, f)


def read_file(filename="alumnos.stu"):
    try:
        with open(f"data/{filename}", "rb") as f:
            saved_list = pickle.load(f)
        return saved_list
    except FileNotFoundError:
        return []
