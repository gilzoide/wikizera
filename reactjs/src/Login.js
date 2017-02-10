import React from 'react';

import bindMethod from './bindMethod.js';
import { Modal, FormGroup, ControlLabel, FormControl, Form, NavItem,
		Col, NavDropdown, Button, Checkbox, MenuItem } from 'react-bootstrap';

class LoginModal extends React.Component {
	constructor (props) {
		super (props);
		this.state = { email: '', password: '', remember: false };
		bindMethod (this, 'tryLogin');
		bindMethod (this, 'handleChange');
		bindMethod (this, 'handleCheckbox');
	}

	tryLogin (e) {
		// previne o redirecionamento da url
		e.preventDefault ();
		if (this.state.email && this.state.password) {
			return this.props.askLogin (this.state.email, this.state.password, this.state.remember)
			.then (this.props.close);
		}
	}

	handleChange (e) {
		this.setState ({ [e.target.name]: e.target.value });
	}

	handleCheckbox (e) {
		this.setState ({ [e.target.name]: e.target.checked });
	}

	render () {
		return (
			<Modal show={this.props.show} onHide={this.props.close}>
				<Modal.Header closeButton>
					<Modal.Title>Login</Modal.Title>
				</Modal.Header>
				<Modal.Body>
					<Form horizontal onSubmit={this.tryLogin}>
						<FormGroup controlId="login-email">
							<Col componentClass={ControlLabel} sm={2}>e½</Col>
							<Col sm={10}>
								<FormControl type="email" name="email"
											 onChange={this.handleChange} />
							</Col>
						</FormGroup>
						<FormGroup controlId="login-password">
							<Col componentClass={ControlLabel} sm={2}>Senha</Col>
							<Col sm={10}>
								<FormControl type="password" name="password"
											 onChange={this.handleChange} />
							</Col>
						</FormGroup>
						<FormGroup controlId="login-remember">
							<Col sm={10} smOffset={2}>
								<Checkbox name="remember" checked={this.state.remember}
								          onChange={this.handleCheckbox}>
									Lembrar
								</Checkbox>
							</Col>
						</FormGroup>
						<Button type="submit">Login</Button>
					</Form>
				</Modal.Body>
			</Modal>
		);
	}
}

class LoginNavItem extends React.Component {
	constructor (props) {
		super (props);
		bindMethod (this, 'handleSelect');
	}

	handleSelect (ev) {
		switch (ev) {
			case "logout":
				this.props.logout();
				break;
			default: break;
		}
	}

	render () {
		const login = this.props.user ?
				<NavDropdown title={this.props.user.email} id="login-nav-dropdown"
				             onSelect={this.handleSelect}>
					<MenuItem divider />
					<MenuItem eventKey="logout">Logout</MenuItem>
				</NavDropdown> :
				<NavItem onClick={this.props.open}>
					Login
				</NavItem>;

		return (
			login
		);
	}
}

export { LoginModal, LoginNavItem };
