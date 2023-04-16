import Head from 'next/head';
import * as React from 'react';
import Image from 'next/image';
import { Inter } from 'next/font/google';
import styles from '@/styles/Home.module.css';
import Appbar from '@/components/Appbar';
import { Box } from '@mui/material';
import { TextField } from '@mui/material';
import { MenuItem } from '@mui/material';
import { Typography } from '@mui/material';
import FormControl from '@mui/material/FormControl';
import { FormLabel } from '@mui/material';
import { useState } from 'react';
import { DemoContainer } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs, { Dayjs } from 'dayjs';
import { Button } from '@mui/material';
import { start } from 'repl';
import CircularProgress from '@mui/material/CircularProgress';

//axios
import axios from 'axios';

//

const inter = Inter({ subsets: ['latin'] });

const field = [
  {
    value: '1',
    label: 'Mean Risk Portfolio Optimization using historical estimates.',
  },
  {
    value: '2',
    label: 'Mean Risk Portfolio Optimization using historical estimates.',
  },
  {
    value: '3',
    label: 'Mean Risk Portfolio Optimization using historical estimates.',
  },
  {
    value: '4',
    label: 'Mean Risk Portfolio Optimization using historical estimates.',
  },
  {
    value: '5',
    label: 'Mean Risk Portfolio Optimization using historical estimates.',
  },
  {
    value: '6',
    label:'Constraints on Return and Risk Measures',
  }
];

const assets = [
  {
    value: 'JCI',
    label: 'JCI',
  },
  {
    value: 'TGT',
    label: 'TGT',
  },
  {
    value: 'CMCSA',
    label: 'CMCSA',
  },
  {
    value: 'CPB',
    label: 'CPB',
  },
  {
    value: 'MO',
    label: 'MO',
  },
  {
    value: 'APA',
    label: 'APA',
  },
  {
    value: 'MMC',
    label: 'MMC',
  },
  {
    value: 'MMC',
    label: 'MMC',
  },
  {
    value: 'JPM',
    label: 'JPM',
  },
  {
    value: 'ZION',
    label: 'ZION',
  },
  {
    value: 'PSA',
    label: 'PSA',
  },
  {
    value: 'BAX',
    label: 'BAX',
  },
  {
    value: 'BMY',
    label: 'BMY',
  },
  {
    value: 'LUV',
    label: 'LUV',
  },
  {
    value: 'PCAR',
    label: 'PCAR',
  },
  {
    value: 'TXT',
    label: 'TXT',
  },
  {
    value: 'TMO',
    label: 'TMO',
  },
  {
    value: 'DE',
    label: 'DE',
  },
  {
    value: 'MSFT',
    label: 'MSFT',
  },
  {
    value: 'HPQ',
    label: 'HPQ',
  },
  {
    value: 'SEE',
    label: 'SEE',
  },
  {
    value: 'VZ',
    label: 'VZ',
  },
  {
    value: 'CNP',
    label: 'CNP',
  },
  {
    value: 'NI',
    label: 'NI',
  },
  {
    value: 'T',
    label: 'T',
  },
];

// const handleChange = (event: SelectChangeEvent) => {
//   set(event.target.value as string);
// };

export default function Optimizer() {
  const [startDate, setStartDate] = useState<Dayjs | null>(dayjs('2022-04-17'));
  const [endDate, setEndDate] = useState<Dayjs | null>(dayjs('2022-04-17'));
  const [goal, setGoal] = useState<string>('1');
  const [loading, setLoading] = useState<boolean>(false);
  const [assets, setAssets] = useState<string[]>([]);
  const [asset, setAsset] = useState<string>('');
  const [count, setCount] = useState<number>(0);

  const [Plot1, setPlot1] = React.useState<any>(null);
  const [Plot2, setPlot2] = React.useState<any>(null);
  const [Plot3, setPlot3] = React.useState<any>(null);
  const [Plot4, setPlot4] = React.useState<any>(null);
  const [Plot5, setPlot5] = React.useState<any>(null);
  const [Plot6, setPlot6] = React.useState<any>(null);
  const [Plot7, setPlot7] = React.useState<any>(null);
  const [Plot8, setPlot8] = React.useState<any>(null);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('submit');
    console.log(startDate);
    console.log(endDate);
    console.log(goal);
    console.log(assets);
    setLoading(true);
    console.log({
      goal: 1,
      start: startDate?.format('YYYY-MM-DD'),
      end: endDate?.format('YYYY-MM-DD'),
      assets: ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO'],
    });

    axios
      .post(
        `http://localhost:5000/optimizer`,
        {
          goal: 'Mean Risk Portfolio Optimization using historical estimates',
          start: startDate?.format('YYYY-MM-DD'),
          end: endDate?.format('YYYY-MM-DD'),
          assets: ['JCI', 'TGT', 'CMCSA', 'CPB', 'MO'],
        },
        {
          headers: {
            // 'Content-Type': 'multipart/form-data',
            'Content-Type': 'application/json',
          },
        }
      )
      .then((res) => {
        console.log(res.data);
        setLoading(false);
        setPlot1('data:image/png;base64,' + res.data.plot1.toString('base64'));
        setPlot2('data:image/png;base64,' + res.data.plot2.toString('base64'));
        setPlot3('data:image/png;base64,' + res.data.plot3.toString('base64'));
        setPlot4('data:image/png;base64,' + res.data.plot4.toString('base64'));
        setPlot5('data:image/png;base64,' + res.data.plot5.toString('base64'));
        setPlot6('data:image/png;base64,' + res.data.plot6.toString('base64'));
        setPlot7('data:image/png;base64,' + res.data.plot7.toString('base64'));
        setPlot8('data:image/png;base64,' + res.data.plot8.toString('base64'));
      });
  };

  const handleChangeCount = (event: any) => {
    setCount(Number(event.target.value));
    const newAssets = [];
    for (let i = 0; i < Number(event.target.value); i++) {
      newAssets.push('');
    }
    setAssets(newAssets);
  };

  return (
    <>
      <Head>
        <title>Optimizer</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div>
          <Appbar />
          <Box sx={{ m: 1 }}>
            <Typography variant="h6">Portfolio optimisation:</Typography>
            <Typography>
              For a given level of risk, we want to make sure that we are
              getting as much return as possible. In quantitative finance, risk
              is viewed like a resource. Exposing your portfolio to risk
              generates returns over time. In other words, expected return is
              the compensation that we get paid in return for taking on
              uncertainty. The risk and uncertainty around an investment’s
              return is traditionally proxied by the standard deviation of its
              historical returns. There is an approximate and positive
              relationship between risk and return. The more volatile an asset
              is, the higher its historical returns have usually been.
            </Typography>
            <Typography variant="h6">Efficient frontier:</Typography>
            <Typography>
              An efficient frontier is a set of investment portfolios that are
              expected to provide the highest returns at a given level of risk.
              A portfolio is said to be efficient if there is no other portfolio
              that offers higher returns for a lower or equal amount of risk.
              Where portfolios are located on the efficient frontier depends on
              the investor’s degree of risk tolerance. According to the
              mean-variance criterion, Portfolio A is a better choice than
              Portfolio B if E(R)A ≥ E(R)B and σA ≤ σB. In other words,
              investors will prefer Portfolio A if the expected returns for
              Portfolio A are higher than Portfolio B, and Portfolio A’s
              standard deviation is lower than Portfolio B’s
            </Typography>

            <Typography>
              We tried optimising Portfolio using historical data, different
              models , different risk measures. The model Could be Classic
              (historical), BL (Black Litterman) or FM (Factor Model). The
              Objective function, could be MinRisk, MaxRet, Utility or Sharpe.
              The risk aversion factor is not used here since the objective
              function is not utility.
            </Typography>
          </Box>
          <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            autoComplete="off"
          >
            <Box sx={{ ml: 1, p: 1 }}>
              <Typography sx={{ mt: 1 }}>Start Date</Typography>
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                  onChange={(newValue) => setStartDate(newValue)}
                  value={startDate}
                />
              </LocalizationProvider>
            </Box>
            <Box sx={{ ml: 1, p: 1 }}>
              <Typography sx={{ mt: 1 }}>End Date </Typography>
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                  onChange={(newValue) => setEndDate(newValue)}
                  value={endDate}
                />
              </LocalizationProvider>
            </Box>
            <Box sx={{ ml: 1, p: 1 }}>
              <Typography sx={{ mt: 1 }}>Optimization Goal</Typography>
              <TextField
                select
                defaultValue="6"
                variant="filled"
                sx={{ width: '100%' }}
              >
                {field.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Box>
            <Box sx={{ ml: 1, p: 1 }}>
              <Typography variant="h6" sx={{ mt: 1 }}>
                Assets
              </Typography>
              <Box sx={{ display: 'flex' }}>
                <Typography sx={{ m: 1 }}>
                  Enter the number of assets you want to optimize:
                </Typography>
                <TextField
                  value={count}
                  onChange={handleChangeCount}
                  variant="outlined"
                />
              </Box>

              {/* {assets.map((asset, index) => (
                <Box sx={{ display: 'flex' }} key={index}>
                  <Typography sx={{ m: 1 }}>Asset {index + 1}</Typography>
                  <Select
                    value={asset}
                    onChange={(event) => {
                      const newAssets = [...assets];
                      newAssets[index] = event.target.value;
                      setAssets(newAssets);
                    }}
                    variant="outlined"
                  >
                    {assets.map((option) => (
                      <MenuItem key={option.value} value={option.value}>
                        {option.label}
                      </MenuItem>
                    ))}
                  </Select>
                  <TextField
                    value={asset}
                    onChange={(event) => {
                      const newAssets = [...assets];
                      newAssets[index] = event.target.value;
                      setAssets(newAssets);
                    }}
                    variant="outlined"
                  />
                </Box>
              ))} */}

              {assets.map((asset, index) => (
                <Box sx={{ display: 'flex' }} key={index}>
                  <Typography sx={{ m: 1 }}>Asset {index + 1}</Typography>
                  <TextField
                    value={asset}
                    onChange={(event) => {
                      const newAssets = [...assets];
                      newAssets[index] = event.target.value;
                      setAssets(newAssets);
                    }}
                    variant="outlined"
                  />
                </Box>
              ))}
            </Box>
            <Box sx={{ ml: 1, p: 1 }}>
              <Button type="submit" variant="contained">
                Submit
              </Button>
            </Box>
          </Box>
          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'center' }}>
              <CircularProgress />
            </Box>
          )}
          {!loading && (
            <Box>
              <Box
                sx={{
                  display: 'flex',
                  m: 1,
                  flexDirection: 'column',
                  alignItems: 'center',
                }}
              >
                {Plot1 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot1} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot2 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot2} alt="plot" width={800} height={500} />
                  </Box>
                )}

                {Plot5 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot5} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot6 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot6} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot7 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot7} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot8 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot8} alt="plot" width={800} height={500} />
                  </Box>
                )}

                {Plot3 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot3} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot4 && (
                  <Box sx={{ m: 1 }}>
                    <Image src={Plot4} alt="plot" width={800} height={500} />
                  </Box>
                )}
              </Box>
            </Box>
          )}
        </div>
      </main>
    </>
  );
}
