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

    showParametersGroup(select.value);
};
