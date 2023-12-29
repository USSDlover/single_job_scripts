// region PopUp

const numberOfAvailableEl = document.getElementById('available');
const connectToBtn = document.getElementById('connect');

// endregion

// region Connect to Users
/**
 * # The Extension Idea
 * The extension is for automating the connection request for making it easier to extend the network
 *
 * ## Notes
 * 1. The button for connecting will get enabled only if there are some people available for connecting
 * 2. Should be able to search based on the job title and get more specific
 */

const connectBtns = [];

const initConnectBtns = () => {
    const buttons = document.getElementsByTagName('button');
    connectBtns.length = 0;
    connectBtns.push(...Object.entries(buttons).filter(btn => btn[1].innerText === 'Connect'));
    
}

const clickToConnect = async (cncBtn) => {
    return new Promise(resolve => {
        console.log('Connect button');
        cncBtn.click();
        setTimeout(() => resolve(), 1500);
    });
}

const sendRequestWithoutNote = async () => {
    return new Promise(resolve => {
        const sendBtn = document.querySelector('button[aria-label="Send now"]');
        if (sendBtn) {
            console.log('Send req btn');
            sendBtn.click();
            setTimeout(() => resolve(), 1500);
        } else {
            console.log('Couldn\'t find the `Send Now` button');
            resolve();
        }
    });
}

const connectToPeopleInList = async () => {
    for (let i = 0; i < connectBtns.length; i++ ) {
        console.log('Connecting to', i + 1);
        await clickToConnect(connectBtns[i][1]);
        await sendRequestWithoutNote();
    }
}

// endregion

// region Withdraw

const withdrawButtons = [];

const initWithdrawButtons = () => {
    const buttons = document.getElementsByTagName('button');
    withdrawButtons.length = 0;
    withdrawButtons.push(...Object.entries(buttons).filter(btn => btn[1].innerText === 'Withdraw'));
}

const clickToWithdraw = async (cncBtn) => {
    return new Promise(resolve => {
        console.log('Select withdraw from dialog');
        cncBtn.click();
        setTimeout(() => resolve(), 500);
    });
}

// artdeco-button artdeco-button--2 artdeco-button--primary ember-view artdeco-modal__confirm-dialog-btn
const completeTheWithdraw = async () => {
    return new Promise(resolve => {
        const sendBtn = document.getElementsByClassName('artdeco-modal__confirm-dialog-btn')[1];
        if (sendBtn) {
            console.log('User withdrawn');
            sendBtn.click();
            setTimeout(() => resolve(), 1500);
        } else {
            console.log('Couldn\'t find the `Withdraw` button');
            resolve();
        }
    });
}

const withdrawPeopleInList = async () => {
    initWithdrawButtons();

    for (let i = 20; i < withdrawButtons.length; i++ ) {
        console.log(`Withdrawing from ${i + 1} from ${withdrawButtons.length}`);
        await clickToWithdraw(withdrawButtons[i][1]);
        await completeTheWithdraw();
    }
}

// endregion

// region Unfollow

const followButtons = [];

const initUnfollowButtons = () => {
    const buttons = document.getElementsByClassName('artdeco-button--secondary');
    followButtons.length = 0;
    followButtons.push(...Object.entries(buttons).filter(btn => btn[1].innerText === 'Following'));
}

const clickToUnfollow = async (cncBtn) => {
    return new Promise(resolve => {
        console.log('Click the following button');
        cncBtn.click();
        setTimeout(() => resolve(), 500);
    });
}

// artdeco-button artdeco-button--2 artdeco-button--primary ember-view artdeco-modal__confirm-dialog-btn
const completeTheUnfollowing = async () => {
    return new Promise(resolve => {
        const sendBtn = document.getElementsByClassName('artdeco-modal__confirm-dialog-btn')[1];
        if (sendBtn) {
            console.log('User Unfollowed');
            sendBtn.click();
            setTimeout(() => resolve(), 1500);
        } else {
            console.log('Couldn\'t find the `Unfollow` button');
            resolve();
        }
    });
}

const showMore = async () => {
    return new Promise(resolve => {
        document.getElementsByClassName('scaffold-finite-scroll__load-button')[0].click();
        setTimeout(() => resolve(), 1500);
    });
}

const unfollowPeopleInList = async () => {
    initUnfollowButtons();

    for (let i = 0; i < followButtons.length; i++ ) {
        console.log(`Unfollow from ${i + 1} from ${followButtons.length}`);
        await clickToUnfollow(followButtons[i][1]);
        await completeTheUnfollowing();
    }
    await showMore();
    unfollowPeopleInList();
}

// endregion
