import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
  DateInput
} from 'react-admin';

export const CouponEdit: FC = (props) => (
  <Edit {...props}>
    <SimpleForm>
    <TextInput disabled source="id" />

    <TextInput source="email" />
      <TextInput source="first_name" />
      <TextInput source="last_name" />
      <TextInput source="phone" />
      <TextInput source="coupon_id" />
      <BooleanInput source="dress_used" />
      <BooleanInput source="makeup_used" />
      <BooleanInput source="hair_used" />
      <DateInput disabled source="created_date" allowEmpty />
      <TextInput disabled source="hair_scanned_location" allowEmpty />
      <TextInput disabled source="dress_scanned_location" allowEmpty />
      <TextInput disabled source="makeup_scanned_location" allowEmpty />
      <DateInput disabled source="hair_scanned_date" allowEmpty />
      <DateInput disabled source="dress_scanned_date" allowEmpty />
      <DateInput disabled source="created_date" allowEmpty />
    </SimpleForm>
  </Edit>
);
