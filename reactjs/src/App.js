import React from 'react';

import WikiNavbar from './WikiNavbar.js';
import ViewRouter from './ViewRouter.js';
import * as ajax from './ajax.js';
import bindMethod from './bindMethod.js';

class App extends React.Component {
	constructor (props) {
		super (props);
		this.state = { user: null };
		bindMethod (this, 'askLogin');
		bindMethod (this, 'logout');
	}

	askLogin (email, password, remember) {
		return ajax.POST ('/login', {
			email: email,
			password: password,
			remember: remember,
		}).then (json => {
			ajax.GET('/user', {authtoken: json.response.user.authentication_token}).then(json => {
				this.setState ({ user: json.user });
			});
		}).catch(err => {
			if(err.email || err.password) {
				const msg = "Erro no login: email ou senha inválidos";
				console.error (msg);
				alert (msg);
			}
			else throw err;
		});
	}

	logout () {
		return ajax.GET ('/logout', {
			authtoken: this.state.user.authtoken
		}).then (json => {
			this.setState ({ user: null });
			return json;
		});
	}

	render() {
		return (
			<div>
				<WikiNavbar user={this.state.user} askLogin={this.askLogin}
				            logout={this.logout} />
				<ViewRouter user={this.state.user} />
			</div>
		);
	}
}

export default App;
