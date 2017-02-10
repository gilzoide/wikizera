import React from 'react';
import { Router, Route, IndexRoute, hashHistory } from 'react-router';

import MarkdownEditor from './MarkdownEditor.js';
import UserHome from './UserHome.js';
import MyPages from './MyPages.js';

class ViewRouter extends React.Component {
	constructor(props) {
		super(props);
		this.passProps = this.passProps.bind(this);
	}
	passProps(Component, props) {
		return <Component {...this.props} {...props} />
	}
	render () {
		return (
			<Router history={hashHistory} createElement={this.passProps}>
				<Route path="/">
					<IndexRoute component={UserHome} />
					<Route path="test" component={MarkdownEditor} />
					<Route path="my-pages" component={MyPages} />
				</Route>
			</Router>
		);
	}
}

export default ViewRouter;
