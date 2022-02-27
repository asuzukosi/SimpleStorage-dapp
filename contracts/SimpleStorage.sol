// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract SimpleStorage {
    struct Person {
        string name;
        uint256 favoriteNumber; 
    }

    mapping(string=>Person) public people;
    uint256 public favoriteNumber = 5;
    bool public favoriteBool = true;
    string public favoriteString = "My string";
    int32 public favoriteInt = 45;
    address public favoriteAddress;
    
    constructor() {
        favoriteAddress = msg.sender;
    }

    function storeFavoriteNumber(uint _new_value) public {
        favoriteNumber = _new_value;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        Person memory _person = Person(_name, _favoriteNumber);
        people[_name] = _person;
    }

    function getFavoriteNumber() public view returns (uint256){
        return favoriteNumber;
    }
}