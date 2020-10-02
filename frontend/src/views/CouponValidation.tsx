import React, { FC, useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';

const styles = makeStyles((theme) => ({
  container: {
    color: 'black',
    direction: 'rtl',
  },
  link: {
    color: 'black',
  },
  title: {
    color: 'black',
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

export const CouponValidation: FC = () => {
  const { couponId } = useParams<{ couponId: string }>();
  const [loading, setLoading] = useState(true);
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const [usedError, setUsedError] = useState(false);
  const [wrongParamsError, setWrongParamsError] = useState(false);

  const [emailError, setEmailError] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const classes = styles();

  const onSubmit = () => {
    setUsedError(false);
    setWrongParamsError(false);

    let url = '/api/v1/validate';
    const response = fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        phone: phone,
        coupon_id: couponId,
        password: password,
      }),
    })
      .then((response) => {
        if (response.ok) setShowSuccess(true);
        else if (response.status === 409) {
          setUsedError(true);
        } else {
          setWrongParamsError(true);
        }
      })
      .catch((err) => {
        console.info(err);
      });
  };

  useEffect(() => {}, []);

  if (showSuccess) return <h1 style={{ color: 'black' }}>Ok</h1>;

  return (
    <Container className={classes.container}>
      <h3 className={classes.link}>אנא הכניסו פרטים לאישור הקופון</h3>
      <div className={classes.input}>
        <TextField
          autoComplete="new-password"
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
          autoComplete="new-password"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          style={{ width: '17rem' }}
          id="standard-basic2"
          label="טלפון"
          variant="outlined"
        />
      </div>
      <div className={classes.input}>
        <TextField
          autoComplete="new-password"
          value={password}
          type="password"
          onChange={(e) => setPassword(e.target.value)}
          style={{ width: '17rem' }}
          id="standard-basic2"
          label="סיסמא"
          variant="outlined"
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
      {usedError && (
        <h3 style={{ color: 'red' }}>הקופון אינו זמין או שומש בעבר</h3>
      )}
      {wrongParamsError && <h3 style={{ color: 'red' }}>הנתונים שגויים</h3>}
    </Container>
  );
};
