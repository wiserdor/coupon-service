import React from 'react';
import { create } from 'jss';
import rtl from 'jss-rtl';
import {
  StylesProvider,
  jssPreset,
  createMuiTheme,
  ThemeProvider,
} from '@material-ui/core/styles';

const RTL = (props: any) => {
  // Configure JSS
  const jss = create({ plugins: [...jssPreset().plugins, rtl()] });
  const theme = createMuiTheme({
    direction: 'rtl',
  });
  return (
    <ThemeProvider theme={theme}>
      <StylesProvider jss={jss}>{props.children}</StylesProvider>
    </ThemeProvider>
  );
};

export default RTL;
