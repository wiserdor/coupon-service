// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  ExportButton,
  EmailField,
  CreateButton,
  EditButton,
  Toolbar,
} from 'react-admin';
import ImportButton from '../import';

const ListActions = (props: any) => {
  const {
    className,
    basePath,
    total,
    resource,
    currentSort,
    filterValues,
    exporter,
  } = props;
  return (
    <div>
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
    </div>
  );
};

export const VendorList: FC = (props) => (
  <List
    actions={<ListActions />}
    style={{ overflowY: 'scroll', width: '84vw', direction: 'ltr' }}
    {...props}
  >
    <Datagrid rowClick="edit">
      <TextField disabled source="id" />
      <TextField source="email" />
      <TextField source="name" />
      <TextField source="phone" />
      <EditButton />
    </Datagrid>
  </List>
);
