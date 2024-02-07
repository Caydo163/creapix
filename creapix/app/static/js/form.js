window.onload = (event) => {
    const select = document.querySelector('select[name="transform_type"');

    select.addEventListener('change', (event) => {
        document.querySelectorAll('.parameters-group').forEach((element) => {
            console.log(element.id, element);
            if (element.id == event.target.value) {
                element.classList.remove('d-none');
            } else {
                element.classList.add('d-none');
            }
        });
    });
};
