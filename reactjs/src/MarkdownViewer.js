import React from 'react';
import { Panel } from 'react-bootstrap';
import { markdown } from 'markdown';

class MarkdownViewer extends React.Component {
	render () {
		const htmlFromMarkdown = markdown.toHTML (this.props.text);
		return (
			<Panel>
				<div dangerouslySetInnerHTML={{__html: htmlFromMarkdown}} />
			</Panel>
		);
	}
}

export default MarkdownViewer;
