
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(filename):
    #leer los dos Csv
    batch1= read_csv_to_dict(filename)
    batch2=read_csv_to_dict('grocery_batch_1.csv')
    #lee los datos de grocery_batch_1
    for row2 in batch2:
        producto_2 = row2['Name']
        cantidad_2 = int(row2['Quantity'])
        existe = False
        #recorre sample_grocery
        for producto_1 in batch1:
            #verifica si existe el producto y suma las cantidades
            if producto_1['Name'] == producto_2:
                existe = True
                producto_1['Quantity'] = str(int(producto_1['Quantity']) + cantidad_2)
                break
        #si no exite agregar al nuevo CSV
        if not existe:
            batch1.append(row2)
    #crea el nuevo CSV
    write_list_of_dicts_to_csv("grocery_db.csv", batch1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv')
    