#nomor3
def duplicate(data):
    new_list = []

    for item in data:
        new_list.append(item)
        new_list.append(item)

    return new_list
hasil_duplikat = duplicate(["Pepaya","Mangga","Pisang","Durian","Jambu"])

print(hasil_duplikat)

