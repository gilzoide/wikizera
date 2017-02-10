import React from 'react';
import { Jumbotron } from 'react-bootstrap';

function BemVindo(props) {
  return <Jumbotron componentClass="h1">Bem vindo, {props.user.username}</Jumbotron>;
}

class UserHome extends React.Component {
  render() {
    return (
      this.props.user ? <BemVindo user={this.props.user} /> : null
    );
  }
}

export default UserHome;
