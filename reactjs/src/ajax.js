import request from 'request-promise';

const backendAddress = "http://localhost:5000";

/// Callback de erro padrão: console.error
function defaultErrCallback (err) {
	console.error (`[wikizera] Request failed: ${err}`);
}

/// Função auxiliar para construir requisições quaisquer, retornando o promise
// com o JSON ou soltando exceção no caso de erros (qualquer JSON com campo
// "error" entra nisso, mesmo com status 200 OK)
function send_request (method, path, body, qs) {
	const endpoint = path.startsWith ('/') ? backendAddress + path : path;
	return request({
		method: method,
		uri: endpoint,
		body: body,
		qs: qs,
		simple: false,
		json: true,
	})
	// dá throw em erros
	.then (json => {
		const erro = json.error || (json.response && json.response.errors);
		if (erro) throw erro;
		return json;
	});
}

function GET (path, qs) {
	return send_request ('GET', path, undefined, qs);
}
function POST (path, body) {
	return send_request ('POST', path, body, undefined);
}


export { GET, POST, defaultErrCallback };
