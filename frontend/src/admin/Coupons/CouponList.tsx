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
  CreateButton,
  ExportButton,
  Toolbar
} from 'react-admin';
import ImportButton from '../import'

const ListActions = (props:any) => {
    const { 
      className, 
      basePath, 
      total, 
      resource, 
      currentSort, 
      filterValues, 
      exporter 
    } = props;
    return (
      <Toolbar className={className}>
        <CreateButton basePath={basePath} />
        <ExportButton
          disabled={total === 0}
          resource={resource}
          sort={currentSort}
          filter={filterValues}
          exporter={exporter}
        />
        <ImportButton {...props} />
      </Toolbar>
    );
  };

export const CouponList: FC = (props) => (
  <List actions={<ListActions />} style={{ overflowY: 'scroll', width: '84vw', direction:'ltr' }} {...props}>
    <Datagrid rowClick="edit" >
      <TextField source="id" />
      <EmailField source="email" />
      <TextField source="name" />
      <TextField source="coupon_id" />
      <BooleanField source="dress_used" />
      <BooleanField source="makeup_used" />
      <BooleanField source="hair_used" />
      <DateField source="created_date" allowEmpty />
      <TextField source="hair_scanned_location" allowEmpty />
      <TextField source="dress_scanned_location" allowEmpty />
      <TextField source="makeup_scanned_location" allowEmpty />
      <DateField source="hair_scanned_date" allowEmpty />
      <DateField source="dress_scanned_date" allowEmpty />
      <DateField source="created_date" allowEmpty />
      <EditButton />
    </Datagrid>
  </List>
);
