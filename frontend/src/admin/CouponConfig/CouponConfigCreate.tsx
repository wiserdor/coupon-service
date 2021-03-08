import React, { FC } from 'react';
import { Create, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const CouponConfigCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <NumberInput source="max_coupons_per_user" />
      <TextInput source="hair_password" />
      <TextInput source="dress_password" />
      <TextInput source="makeup_password" />
      <TextInput source="email_template"  />
    </SimpleForm>
  </Create>
);
