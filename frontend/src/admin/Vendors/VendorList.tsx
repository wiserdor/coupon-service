// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  ExportButton,
  CardActions,
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
      <CardActions className={className}>
        <CreateButton  basePath={basePath}  />
        <ExportButton
          disabled={total === 0}
          resource={resource}
          sort={currentSort}
          filter={filterValues}
          exporter={exporter}
        />
        <ImportButton {...props} />
      </CardActions>
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
      <TextField source="first_name" />
      <TextField source="last_name" />
      <TextField source="phone" />
      <EditButton />
    </Datagrid>
  </List>
);
