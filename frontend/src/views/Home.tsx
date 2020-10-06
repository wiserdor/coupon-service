import React, { FC, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import Title from './Title';

const styles = makeStyles((theme) => ({
  container: {
    color: '#333333',
    direction: 'rtl',
  },
  link: {
    color: '#333333',
    fontWeight:600,
  },
  title: {
    color: '#333333',
  },
  button: {
    fontSize: '1.5rem',
    fontWeight: 700,
    width: '20rem',
  },
  input: {
    marginBottom: '1rem',
  },
}));

export const Home: FC = () => {
  const [email, setEmail] = useState<string>('');
  const [name, setName] = useState<string>('');
  const [emailError, setEmailError] = useState(false);
  const [nameError, setNameError] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const classes = styles();

  const isMailValid = () => {
    //return /^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[A-Za-z]+$/.test(email);
    return true;
  };

  const onSubmit = (e: any) => {
    e.preventDefault();
    if (!isMailValid()) {
      setEmailError(true);
      return;
    } else {
      setEmailError(false);
    }
    if (name.length === 0) {
      setNameError(true);
      return;
    } else {
      setNameError(false);
    }
    let url = '/api/v1/coupons';
    fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: email, name: name }),
    })
      .then((response) => {
        if (response.ok) setShowSuccess(true);
      })
      .catch((err) => {
        console.info(err);
      });
  };

  if (showSuccess)
    return (
      <Container className={classes.container}>
        <h1 className={classes.title}>קופון נשלח בהצלחה</h1>
      </Container>
    );

  return (
    <Container className={classes.container}>
      <Title />
      <h3 className={classes.link}>הכניסו פרטים לקבלת הקופון</h3>
      <div className={classes.input}>
        <TextField
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ width: '17rem' }}
          id="standard-basic"
          label="אימייל"
          variant="outlined"
          error={emailError}
        />
      </div>
      <div className={classes.input}>
        <TextField
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{ width: '17rem' }}
          id="standard-basic2"
          label="שם מלא"
          variant="outlined"
          error={nameError}
        />
      </div>
      <Button
        onClick={onSubmit}
        className={classes.button}
        variant="contained"
        color="secondary"
      >
        שלח
      </Button>
    </Container>
  );
};
