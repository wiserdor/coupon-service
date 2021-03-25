import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
} from 'react-admin';

export const VendorCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="email" />
      <TextInput source="first_name" />
      <TextInput source="last_name" />
      <TextInput source="phone" />
    </SimpleForm>
  </Create>
);
