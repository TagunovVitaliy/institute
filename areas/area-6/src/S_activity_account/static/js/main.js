function CreateScientificActivity() {
    const name = $('#name').val();
    const description = $('#description').val();

    $.ajax({
		url:    	's_activity',
		method:		'POST',
		cache: 		false,
		data:   	JSON.stringify({'name': name, 'description': description}),
		contentType: 'application/json; charset=utf-8',
        dataType:	'html',
		success: function(data) {
			$('body').html(data);
		}
	});
}

function AddTeacher() {
    const s_activity_id = $('#s_activity_id').val();
    const name = $('#name').val();
    const surname = $('#surname').val();
    const role = $('#role').val();

    $.ajax({
		url:    	'teacher',
		method:		'POST',
		cache: 		false,
		data:   	JSON.stringify({'s_activity_id': s_activity_id, 'name': name, 'surname': surname,
            'role': role}),
		contentType: 'application/json; charset=utf-8',
        dataType:	'html',
		success: function(data) {
			$('body').html(data);
		}
	});
}

function AddUser() {
    const teacher_id = $('#teacher_id').val();
    const name = $('#name').val();

    $.ajax({
		url:    	'user',
		method:		'POST',
		cache: 		false,
		data:   	JSON.stringify({'teacher_id': teacher_id, 'name': name}),
		contentType: 'application/json; charset=utf-8',
        dataType:	'html',
		success: function(data) {
			$('body').html(data);
		}
	});
}

