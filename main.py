import os
import cv2
 
def resize_img(DATADIR, data_k, img_size):

    w = img_size[0]
    h = img_size[1]
    '' 'Establezca el tamaño de píxel objetivo, aquí configurado en 300' ''
    path = os.path.join(DATADIR, data_k)
         # Devuelva el nombre de todos los archivos en la ruta de acceso y el nombre de la carpeta,
    img_list = os.listdir(path)
 
    for i in img_list:

        if i.endswith('.jpg'):

                         # Llame a cv2.imread para leer en la imagen, el formato de lectura es IMREAD_COLOR
            img_array = cv2.imread((path + '/' + i), cv2.IMREAD_COLOR)
                         # Llame a la función cv2.resize para cambiar el tamaño de la imagen
            new_array = cv2.resize(img_array, (w, h), interpolation=cv2.INTER_CUBIC)
            img_name = str(i)
            '' 'C:/Users/Supervisor/Desktop/convertirimagenes/query' ''
            save_path = path + '_new/'
            if os.path.exists(save_path):
                print(i)
                '' 'Llame a la función cv.2 imwrite para guardar la imagen' ''
                save_img=save_path+img_name
                cv2.imwrite(save_img, new_array)
            else:
                os.mkdir(save_path)
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)
 
 
if __name__ == '__main__':
         # Establecer ruta de imagen
    DATADIR = "C:/Users/Supervisor/Desktop/convertirimagenes/"
    data_k = 'query'
         # Nuevo tamaño que necesita ser modificado
    img_size = [640, 480]
    resize_img(DATADIR, data_k, img_size)