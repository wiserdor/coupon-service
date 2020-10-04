// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  EmailField,
  EditButton,
} from 'react-admin';

export const VendorList: FC = (props) => (
  <List style={{ overflowY: 'scroll', width: '84vw', direction:'ltr' }} {...props}>
    <Datagrid rowClick="edit">
      <TextField disabled source="id" />
      <TextField source="email" />
      <TextField source="name" />
      <TextField source="phone" />
      <EditButton />
    </Datagrid>
  </List>
);
