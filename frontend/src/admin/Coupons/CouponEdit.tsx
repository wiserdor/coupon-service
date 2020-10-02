import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
} from 'react-admin';

export const CouponEdit: FC = (props) => (
  <Edit {...props}>
    <SimpleForm>
    <TextInput source="email" />
      <TextInput source="name" />
      <TextInput source="coupon_id" />
      <BooleanInput source="dress_used" />
      <BooleanInput source="makeup_used" />
      <BooleanInput source="hair_used" />
    </SimpleForm>
  </Edit>
);
