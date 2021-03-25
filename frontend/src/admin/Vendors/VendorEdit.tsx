import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
} from 'react-admin';

export const VendorEdit: FC = (props) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput source="email" />
      <TextInput source="first_name" />
      <TextInput source="last_name" />
      <TextInput source="phone" />
    </SimpleForm>
  </Edit>
);
