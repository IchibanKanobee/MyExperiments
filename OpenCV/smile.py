import cv2
import os

def list_files_in_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    else:
        print("Folder doesn't exist or is not a directory.")
        return []
        

folder_path =  '/media/HDD/Datasets/Humans'
file_list = list_files_in_folder(folder_path)
print (file_list)

# Load pre-trained models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

for f in file_list:
    # Load input image
    path = os.path.join(folder_path, f)
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Sort faces based on size (area)
    faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)

    # Get the rectangle with the highest probability of containing a face 
    if len(faces) > 0:
        x, y, w, h = faces[0]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Detect smiles within the highest probability face
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        
        # Check if smile is detected
        if len(smiles) > 0:
            cv2.putText(img, 'Smiling', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        else:
            cv2.putText(img, 'Not Smiling', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    # Display the output image
    cv2.imshow('Smile Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
      
