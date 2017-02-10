import React from 'react';
import { ListGroup, ListGroupItem } from 'react-bootstrap';

import * as ajax from './ajax.js';

class MyPages extends React.Component {
  constructor(props) {
    super(props);
    ajax.GET('/my-pages', {
      authtoken: props.user.authtoken
    }).then(json => {
      this.children = json.map(pagina => (
        <ListGroupItem key={pagina.id} href='#/my-pages/{pagina.id}'>{pagina.name}</ListGroupItem>
      ));
    });
  }
	render() {
		return (
			<ListGroup>
        {this.children}
			</ListGroup>
		);
	}
}

export default MyPages;
