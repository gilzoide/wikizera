import React from 'react';

import { Grid, Row, Col, FormControl, Button } from 'react-bootstrap';
import MarkdownViewer from './MarkdownViewer.js';
import './editor.css';

const placeholder = "Insira seu **markdown** [aqui](#/test)";

class EditorForm extends React.Component {
	constructor(props) {
		super(props);
		this.onChange = this.onChange.bind(this);
	}

	onChange(e) {
		this.props.updateContent(e.target.value);
	}

	render() {
		return (
			// const save_stuff = this.props.user ? <Button type="submit">Vai!</Button>
			<form>
				<FormControl componentClass="textarea" rows="20" placeholder={placeholder}
							       onChange={this.onChange} name="content" />
				{save_stuff}
			</form>
		);
	}
}

class MarkdownEditor extends React.Component {
	constructor(props) {
		super(props);
		this.state = { content: placeholder };
		this.updateContent = this.updateContent.bind(this);
	}

	updateContent(newContent) {
		this.setState({ content: newContent });
	}

	render() {
		return (
			<Grid>
				<Row>
					<Col xs={12} md={6}>
						<EditorForm updateContent={this.updateContent} user={this.props.user} />
					</Col>
					<Col xs={12} md={6}>
						<MarkdownViewer className="fill" text={this.state.content || placeholder} />
					</Col>
				</Row>
			</Grid>
		);
	}
}

export default MarkdownEditor;
