# Complete Product Detection Model
Tensorflow Keras Model<br>
ResNet50 : Acc = 0.99 , Val_acc = 0.91<br>
Final Score : 0.738<br>
Link Model : <a href='https://drive.google.com/file/d/1-5H5ayFjygmFH4d-7qV2VwbQ7VSbtDMZ/view?usp=sharing'>ResNet50</a><br>
Kekurangan : <strong>Overfit</strong>
## Model Preparation
```
from tensorflow.keras.applications.resnet import preprocess_input
```
## Usage
```
import numpy as np
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load Image
image = load_img('...IMAGE DIR/IMAGE FILE')
image_array = np.expand_dims(img_to_array(image), axis = 0)

# Preprocess Image
prep_image = preprocess_input(image_array)

# Load Model
model = load_model('...DIR/ResNet50_1-Adam-Final.h5')

# Predict
pred = model.predict(prep_image)

# Get Classes
print(np.argmax(pred))
```