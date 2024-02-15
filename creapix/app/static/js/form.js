window.onload = (event) => {
    const select = document.querySelector('select[name="transform_type"');

    function showParametersGroup(value) {
        document.querySelectorAll('.parameters-group').forEach((element) => {
            if (element.id == value) {
                element.classList.remove('d-none');
            } else {
                element.classList.add('d-none');
            }
        });
    }

    select.addEventListener('change', (event) => {
        showParametersGroup(event.target.value);
    });

    let urlList = [];
    
    document.getElementById('addButton').onclick = () => {
        
        var hiddenDiv = document.getElementById('images');

        var image = document.createElement('img');
        image.src = document.getElementById('id_url').value;
        image.width = 50;
        image.height = 50;
        
        hiddenDiv.appendChild(image);
        
        urlList.push(image.src);
    };

    document.getElementById('submit').onclick = () => {

        var dataTransfer = new DataTransfer();

        var files = document.getElementById('id_files').files;
        let filesArray = Array.from(files);

        urlList.forEach(function (url) {
            fetch(url)
            .then(res => res.blob())
            .then(blob => {
                let file = new File([blob], 'image.jpg', blob);
                filesArray.push(file);
            });
        });
        
        filesArray.forEach(file => dataTransfer.items.add(file));

        document.getElementById('id_files').files = dataTransfer.files;
        console.log(document.getElementById('id_files').files);
    }

    showParametersGroup(select.value);
};
