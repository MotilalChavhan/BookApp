const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

const alert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible d-flex align-items-center" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}
let status = "{{ status }}";
let message = "{{ message }}";
document.querySelector('#addmembers').addEventListener('click', {
	if (status == 'fail') {
		alert(message, 'danger');
		return;
	}
	alert(message, status);
})