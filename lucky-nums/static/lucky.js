async function processForm(evt) {
	evt.preventDefault();
	$('#name-err, #email-err, #year-err, #color-err').empty();

	let name = $('#name').val();
	let email = $('#email').val();
	let year = $('#year').val();
	let color = $('#color').val();

	const newUserResponse = await axios.post(
		`http://localhost:5000/api/get-lucky-num`,
		{
			name,
			email,
			year,
			color,
		}
	);
	console.log('after');
	let ax_resp = newUserResponse.data;
	handleResponse(ax_resp);

	return;
}

function handleResponse(resp) {
	$('#lucky-results').empty();

	if (resp.errors) {
		for (key of Object.keys(resp.errors)) {
			$(`#${key}-err`).append(`${Object.values(resp.errors[key])}`);
		}
	} else {
		$('#lucky-results').append(
			`<p>Your lucky number is ${resp.num['num']} (Fun fact: ${resp.num['fact']})</p>`
		);
		$('#lucky-results').append(
			`<p>Your birth year is ${resp.year['year']} (Fun fact: ${resp.year['fact']})</p>`
		);
		$('#lucky-form').trigger('reset');
	}
}

$('#lucky-form').on('submit', processForm);
