import React from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';

import { LoginModal, LoginNavItem } from './Login';

function UserTools(props) {
	return (<Nav>
		<NavItem href='#/my-pages'>Minhas Páginas</NavItem>
	</Nav>);
}

class WikiNavbar extends React.Component {
	constructor(props) {
		super (props);
		this.state = { showModal: false };
		this.open = this.open.bind (this);
		this.close = this.close.bind (this);
	}
	open() {
		this.setState ({ showModal: true });
	}
	close() {
		this.setState ({ showModal: false });
	}

	render() {
		const userTools = this.props.user ? <UserTools user={this.props.user} /> : null;
		return (
			<div>
				<LoginModal show={this.state.showModal} close={this.close}
				            askLogin={this.props.askLogin}/>
				<Navbar>
					<Navbar.Header>
						<Navbar.Brand>
							<a href='#'>Wikizera</a>
						</Navbar.Brand>
						<Navbar.Toggle />
					</Navbar.Header>
					<Navbar.Collapse>
						<Nav>
							<NavItem href="#/test">Testar</NavItem>
						</Nav>
						{userTools}
						<Nav pullRight >
							<LoginNavItem user={this.props.user} open={this.open}
							              logout={this.props.logout} />
						</Nav>
					</Navbar.Collapse>
				</Navbar>
			</div>
		);
	}
}

export default WikiNavbar;
