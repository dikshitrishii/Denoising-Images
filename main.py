# Necessry imports
import tensorflow as tf
from tensorflow.keras.models import load_model
import glob
import imageio
import numpy as np
import os

# PSNR matrix
def psnr_metric(y_true, y_pred):
    return tf.image.psnr(y_true, y_pred, max_val=1.0)

# Load the model with the PSNR value matrixx
trained_model = load_model('Models/mymodel2.h5', custom_objects={'psnr_metric': psnr_metric})


#Image Enhancement
def ImageEnhancing(img, index, flag):
    if index == 0:
        return img

    elif flag == 1:
        h, w, c = img.shape
        test = trained_model.predict(img.reshape(1, h, w, 3))
        temp = img / 255
        image = temp + ((test[0,:,:,:] * temp)*(1-temp))
        psnr_value = psnr_metric(tf.convert_to_tensor(img, dtype=tf.float32), tf.convert_to_tensor(image * 255, dtype=tf.float32)).numpy()
        print(f"PSNR: {psnr_value:.4f}")
        index = index - 1
        flag = 0
        return ImageEnhancing(image, index, flag)

    else:
        h, w, c = img.shape
        temp = trained_model.predict(img.reshape(1, h, w, 3))
        image = img + ((temp[0,:,:,:] * img)*(1-img))
        psnr_value = psnr_metric(tf.convert_to_tensor(img, dtype=tf.float32), tf.convert_to_tensor(image, dtype=tf.float32)).numpy()
        print(f"PSNR: {psnr_value:.4f}")
        index = index - 1
        return ImageEnhancing(image, index, flag)
    

# Load images from the specified directory ./test/low
path = 'test/low'
all_files = glob.glob(path + "/*")
x = list()
all_files.sort()
for fileName in all_files:
    img = imageio.imread(fileName)
    x.append(img)
img = np.array(x)


# Enhance the first image and save the result
# IT WILL GIVE OUTPUT FOR THE FIRST IMAGE INSERTED, FOR OTHER IMAGE CHANGE THE INDEX

Image = img[0]
enhanced_image = ImageEnhancing(Image, 8, 1)

#Specifying the output path i.e ./test/predicted
output_path = 'test/predicted'
os.makedirs(output_path, exist_ok=True)


# Saving the output and printing
output_file = os.path.join(output_path, 'enhanced_image.png')
imageio.imwrite(output_file, (enhanced_image * 255).astype(np.uint8))
print(f"Output Enhanced image is saved to {output_file}")