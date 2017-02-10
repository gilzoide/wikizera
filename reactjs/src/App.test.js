import React from 'react';
import { shallow } from 'enzyme';

import App from './App.js';

it ('Testa se renderiza', () => {
  const app = shallow (<App />);
});
