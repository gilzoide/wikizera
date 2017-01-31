import 'whatwg-fetch';

const backendAddress = "http://127.0.0.1:5000";

/// Callback de erro padrão: console.error
function defaultErrCallback (err) {
	console.error (`[wikizera] Request failed: ${err}`);
}

/// Função auxiliar para construir requisições quaisquer, com os callbacks
// que quiser (o de erro é opcional)
function send_request (method, path, body, callback, errCallback) {
	const endpoint = path.startsWith ('/') ? backendAddress + path : path;
	fetch (endpoint, {
		method: method,
		body: JSON.stringify (body),
	})
	.then (res => res.json ())
	.then (callback)
	.catch (errCallback || defaultErrCallback);
}

function GET (path, callback, errCallback) {
	send_request ('GET', path, undefined, callback, errCallback);
}
function POST (path, body, callback, errCallback) {
	send_request ('POST', path, body, callback, errCallback);
}


export { GET, POST };
