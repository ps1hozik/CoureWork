from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete
from database import get_async_session

from .schemas import OrganizationCreate, OrganizationUpdate
from .models import Organization
from auth.models import User
from manager.utils import check_role

router = APIRouter(
    prefix="/organization",
    tags=["Organization"],
)


@router.post("/", status_code=201)
async def create(
    current_id: int,
    data: OrganizationCreate,
    session: AsyncSession = Depends(get_async_session),
):

    await check_role(current_id, session)
    query = select(Organization).where(Organization.code == data.code)
    organization: Organization | None = await session.scalar(query)
    if organization != None:
        raise HTTPException(
            status_code=401,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization with code '{data.code}' already exist!",
            },
        )
    stmt = insert(Organization).values(**data.dict(), manager_id=current_id)
    await session.execute(stmt)
    await session.commit()
    query = select(Organization).where(Organization.code == data.code)
    organization: Organization | None = await session.scalar(query)
    stmt = select(User).where(User.id == current_id)
    user: User | None = await session.scalar(stmt)
    user.organization_id = organization.id
    await session.commit()

    return {
        "status": "success",
        "data": {"id": organization.id},
        "details": "Successful createtion",
    }


@router.patch("/{id}")
async def update(
    id: int,
    current_id: int,
    data: OrganizationUpdate,
    session: AsyncSession = Depends(get_async_session),
):

    try:
        await check_role(current_id, session)
        stmt = select(Organization).where(Organization.id == id)
        organization: Organization | None = await session.scalar(stmt)
        if data.name:
            organization.name = data.name
        if data.code:
            organization.code = data.code
        if data.description:
            organization.description = data.description
        await session.commit()
        return {
            "status": "success",
            "data": organization,
            "details": "Successful update",
        }
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization with code: {data.code} already exist!",
            },
        )
    except AttributeError:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization {id} dosen't exist!",
            },
        )
    except:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None,
            },
        )


@router.get("/{id}")
async def get_by_id(
    id: int, current_id: int, session: AsyncSession = Depends(get_async_session)
):
    await check_role(current_id, session)
    stmt = select(Organization).where(Organization.id == id)
    organization: Organization | None = await session.scalar(stmt)
    if organization == None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization {id} dosen't exist!",
            },
        )
    return {"status": "success", "data": organization, "details": None}


@router.delete("/", status_code=204)
async def delete_by_manager(
    current_id: int, session: AsyncSession = Depends(get_async_session)
):
    await check_role(current_id, session)
    stmt = delete(Organization).where(Organization.manager_id == current_id)
    result: Result = await session.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization {id} dosen't exist!",
            },
        )
    await session.commit()
    return {"status": "success", "data": None, "details": "Successful remove"}


# @router.get("/get_by_code/{code}")
# async def get_by_code(code: str, session: AsyncSession = Depends(get_async_session)):

#     stmt = select(Organization).where(Organization.code == code)
#     organization: Organization | None = await session.scalar(stmt)
#     if organization == None:
#         raise HTTPException(
#             status_code=404,
#             detail={
#                 "status": "error",
#                 "data": None,
#                 "details": "Organozation dosen't exist",
#             },
#         )
#     return {"status": "success", "data": organization, "details": None}
