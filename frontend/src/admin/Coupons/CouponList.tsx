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

export const CouponList: FC = (props) => (
  <List {...props}>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <EmailField source="email" />
      <TextField source="name" />
      <TextField source="coupon_id" />
      <BooleanField source="dress_used" />
      <BooleanField source="makeup_used" />
      <BooleanField source="hair_used" />
      <EditButton />
    </Datagrid>
  </List>
);
