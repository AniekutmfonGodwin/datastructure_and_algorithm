class User {
    constructor() {
      this.totalProgress = 0;
    }
    
    get progress() {
      return this.rank < 8 ? this.totalProgress % 100 : 0;
    }
    
    get rank() {
      let rank = Math.floor(this.totalProgress / 100) - 8;
      return rank >= 0 ? rank + 1 : rank;
    }
    
    incProgress(rank) {
      if (rank === 0 || rank < -8 || rank > 8) {
        throw new Error('Rank out of bounds');
      }
      
      if (rank > 0  && this.rank < 0) {
        rank--;
      }
  
      const diff = rank - this.rank;
      this.totalProgress += diff > 0 ? (10 * diff * diff) : diff < 0 ? 1 : 3;
    }
  }
  