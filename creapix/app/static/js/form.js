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

    function addImage(url) {
        const hiddenDiv = document.getElementById('images');

        let image = document.createElement('img');
        image.src = url;
        image.width = 50;
        image.height = 50;
        image.classList.add('rounded', 'm-1');

        hiddenDiv.appendChild(image);
    }

    document.getElementById('add-button').onclick = () => {
        const urlInput = document.getElementById('id_url');

        if(urlInput.value === '') { 
            throw new Error('URL is required');
        }

        addImage(urlInput.value);
        
        let urlList = document.getElementById('id_url_list');
        urlList.value += '£$$£' + urlInput.value ;

        urlInput.value = '';
    };

    document.getElementById('clear-button').onclick = () => {
        clear();
    };

    let urlList = document.getElementById('id_url_list');
    urlList.value.split('£$$£').forEach((url) => {
        if (url !== '') {
            addImage(url);
        }
    });

    showParametersGroup(select.value);

    function clear() {
        const hiddenDiv = document.getElementById('images');
        hiddenDiv.innerHTML = '';
        document.getElementById('id_url_list').value = '';
        document.getElementById('id_files').value = '';
    }
};
