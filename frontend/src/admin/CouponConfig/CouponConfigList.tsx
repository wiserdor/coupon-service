// in src/users.js
import React, { FC } from 'react';
import { Datagrid, EditButton, List, TextField } from 'react-admin';

export const CouponConfigList: FC = (props) => (
  <List
    style={{ overflowY: 'scroll', width: '84vw', direction: 'ltr' }}
    {...props}
  >
    <Datagrid rowClick="edit">
      <TextField source="max_coupons_per_user" />
      <TextField source="hair_password" />
      <TextField source="dress_password" />
      <TextField source="makeup_password" />
      <TextField source="email_template" />
      <EditButton />
    </Datagrid>
  </List>
);
