import React, { Component } from 'react';

import * as ajax from './ajax.js';

class App extends Component {
	constructor (props) {
		super (props);
		this.state = {};
		ajax.GET ('/', (json) => { this.setState ({ oi: json }); });
	}
	render() {
		return (
			<div className="App">
				Oi {this.state.oi}
			</div>
		);
	}
}

export default App;
