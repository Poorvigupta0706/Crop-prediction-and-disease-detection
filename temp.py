@app.route('/crop_disease', methods=['GET', 'POST'])
def crop_disease():
    if request.method == 'POST':
        file = request.files.get('file')  # Using .get() for safety

        if file:
            
            filename = secure_filename(file.filename)

           
            upload_folder = 'static/uploads'
            os.makedirs(upload_folder, exist_ok=True)  
            
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            
            image = Image.open(file_path) 
            img_batch = preprocess_image(image)  

          
            predictions = disease_model.predict(img_batch)
            predicted_class = CLASS_NAMES[np.argmax(predictions)]
            confidence = np.max(predictions) * 100  

            
            return render_template("crop_disease2.html", prediction=predicted_class, confidence=confidence, filename=filename)

    return render_template("crop_disease2.html", prediction=None)
