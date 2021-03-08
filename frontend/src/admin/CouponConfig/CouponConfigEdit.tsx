import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput } from 'react-admin';

export const CouponConfigEdit: FC = (props) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput disabled source="id" />

      <TextInput source="max_coupons_per_user" />
      <TextInput source="hair_password" />
      <TextInput source="dress_password" />
      <TextInput source="makeup_password" />
      <TextInput source="email_template" />
    </SimpleForm>
  </Edit>
);
