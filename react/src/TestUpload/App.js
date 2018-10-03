import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import FileUpload from '@material-ui/icons/FileUpload';
import Add from '@material-ui/icons/Add';
import {testApi} from "../helpers/test";


class App extends Component {
  constructor(props,context) {
    super(props, context)
    this.state = {
      file: null
    };
  };

  handleAddFile = (e) => {
    this.setState({
      file: e.target.files[0]
    })
  };

  handleClick = () => {
    console.log(this.state.file);
    testApi(this.state.file, (cb) => (
      console.log(cb)
    ))
  };


  render() {
    return (
      <div>
        <AppBar position={'static'} color={'primary'}>
          <Toolbar>
            <Typography variant={"title"} color={"inherit"}>
              {"Sample API Call"}
            </Typography>
          </Toolbar>
        </AppBar>
        <Grid container spacing={24}>
          <Grid item xs={12}>
            <div style={{ padding: 20 }}>
              <Grid
                container
                alignItems={'center'}
                justify={'center'}>
                <form noValidate autoComplete={"off"}>
                  <input
                    type={"file"}
                    onChange={this.handleAddFile}
                    style={{display: 'none'}}
                    ref={fileButton => this.fileButton = fileButton}/>
                  <div onClick={() => this.fileButton.click()}>
                      {this.state.file !== null
                        ? <Button variant={"contained"} color={"secondary"}>
                            {this.state.file.name}
                          </Button>
                        : <Button variant={"contained"} color={"secondary"}>
                            {'Select Excel File'}
                            <Add/>
                          </Button>}
                  </div>
                </form>
              </Grid>
            </div>
            {this.state.file !== null
              ? <div style={{ padding: 20 }}>
                  <Grid
                    container
                    alignItems={'center'}
                    justify={'center'}>
                    <div onClick={this.handleClick}>
                      <Button variant={"contained"} color={"primary"}>
                        {'Upload File'}
                        <FileUpload/>
                      </Button>
                    </div>
                    </Grid>
                  </div>
                : null}
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default App;
