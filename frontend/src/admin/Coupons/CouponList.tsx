// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  EmailField,
  EditButton,
  DateField,
} from 'react-admin';

export const CouponList: FC = (props) => (
  <List
    style={{ overflowY: 'scroll', width: '84vw', direction: 'ltr' }}
    {...props}
  >
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <EmailField source="email" />
      <TextField source="first_name" />
      <TextField source="last_name" />
      <TextField source="phone" />
      <TextField source="coupon_id" />
      <BooleanField source="dress_used" />
      <BooleanField source="makeup_used" />
      <BooleanField source="hair_used" />
      <TextField source="dress_vendor" />
      <TextField source="makeup_vendor" />
      <TextField source="hair_vendor" />
      <DateField source="created_date" allowEmpty />
      <TextField source="hair_scanned_location" allowEmpty />
      <TextField source="dress_scanned_location" allowEmpty />
      <TextField source="makeup_scanned_location" allowEmpty />
      <DateField source="hair_scanned_date" allowEmpty />
      <DateField source="dress_scanned_date" allowEmpty />
      <DateField source="makeup_scanned_date" allowEmpty />
      <DateField source="created_date" allowEmpty />
      <EditButton />
    </Datagrid>
  </List>
);
